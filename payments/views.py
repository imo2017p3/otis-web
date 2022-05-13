from django.conf import settings
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from roster.models import Invoice
import stripe


def invoice(request: HttpRequest, invoice_id: int) -> HttpResponse:
	invoice = Invoice.objects.get(pk=invoice_id)
	context = {'invoice': invoice}
	return render(request, "payments/invoice.html", context)


@csrf_exempt
def stripe_config(request: HttpRequest) -> HttpResponse:
	if request.method == 'GET':
		stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
		return JsonResponse(stripe_config, safe=False)
	else:
		return HttpResponseForbidden('Need to use request method GET')


@csrf_exempt
def checkout(request: HttpRequest, quantity: int) -> HttpResponse:
	stripe.api_key = settings.STRIPE_SECRET_KEY
	domain_url = 'http://127.0.0.1:8000'
	if request.method == 'GET':
		checkout_session = stripe.checkout.Session.create(
			client_reference_id=request.user.id if request.user.is_authenticated else None,
			success_url=domain_url + '/payments/success/',
			cancel_url=domain_url + '/payments/cancelled/',
			payment_method_types=['card'],
			mode='payment',
			line_items=[
				{
					'name': 'OTIS Semester',
					'quantity': quantity,
					'currency': 'usd',
					'amount': 24000 * quantity,  # TODO fix this
				}
			]
		)
		return JsonResponse({'sessionId': checkout_session['id']})
	else:
		return HttpResponseForbidden('Need to use request method GET')


@csrf_exempt
def webhook(request: HttpRequest) -> HttpResponse:
	if request.method != 'POST':
		return HttpResponseForbidden("Need to use request method POST")
	stripe.api_key = settings.STRIPE_SECRET_KEY
	endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
	payload = request.body
	sig_header = request.META['HTTP_STRIPE_SIGNATURE']
	event = None

	try:
		event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
	except ValueError:
		# Invalid payload
		return HttpResponse(status=400)
	except stripe.error.SignatureVerificationError:
		# Invalid signature
		return HttpResponse(status=400)

	# Handle the checkout.session.completed event
	if event['type'] == 'checkout.session.completed':
		print("Payment was successful.")
		# TODO: run some custom code here
	return HttpResponse(status=200)


def success(request: HttpRequest) -> HttpResponse:
	return HttpResponse("Successful payment")


def cancelled(request: HttpRequest) -> HttpResponse:
	return HttpResponse("Cancelled payment")