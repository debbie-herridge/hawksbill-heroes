/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripe = Stripe('pk_test_51O7GgWCZm1VhH3EARqX3yyfDFggCawbVEmRC0qNwMgZoXtUUDPqXwY5VQVFiuIzGSJlZWazwMLgz5KtgW1nHVBBK00RDLWUXDJ');

var clientSecret = $('#id_client_secret').text().slice(1, -1);

// Create card detail elements
var elements = stripe.elements();
var style = {
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');


// Handle realtime validation errors
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
        <p>${event.error.message}</p>`;
    $(errorDiv).html(html);
    } else {
        errorDiv.textContent= ''
    }
})

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <p>${result.error.message}</p>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});