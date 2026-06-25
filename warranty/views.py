from django.shortcuts import render

from .forms import WarrantyCheckForm
from .models import ProductWarranty


def get_public_status(product: ProductWarranty):
    if product.status == ProductWarranty.Status.IN_STOCK:
        return {
            'kind': 'info',
            'title': 'Товар оригинальный, но гарантия ещё не активирована',
            'message': 'Серийный номер есть в официальной базе. Гарантия начнётся после продажи и активации.',
        }
    if product.status == ProductWarranty.Status.SOLD:
        if product.is_warranty_active:
            return {
                'kind': 'success',
                'title': 'Товар оригинальный. Гарантия активна',
                'message': f'До окончания гарантии осталось {product.days_left} дней.',
            }
        return {
            'kind': 'warning',
            'title': 'Товар оригинальный, но гарантия истекла',
            'message': 'Срок официальной гарантии по этому серийному номеру завершён.',
        }
    if product.status == ProductWarranty.Status.RETURNED:
        return {
            'kind': 'warning',
            'title': 'Серийный номер найден, но товар отмечен как возврат',
            'message': 'Для уточнения статуса обратитесь в поддержку.',
        }
    if product.status == ProductWarranty.Status.REPLACED:
        return {
            'kind': 'warning',
            'title': 'Серийный номер найден, но товар был заменён',
            'message': 'Для проверки нового устройства обратитесь в поддержку.',
        }
    return {
        'kind': 'danger',
        'title': 'Серийный номер требует проверки',
        'message': 'Обратитесь в поддержку для ручной проверки товара.',
    }


def check_warranty(request):
    result = None
    product = None
    not_found_serial = None

    initial_serial = request.GET.get('serial', '')

    if request.method == 'POST':
        form = WarrantyCheckForm(request.POST)
    else:
        form = WarrantyCheckForm(initial={'serial_number': initial_serial})

    should_check = request.method == 'POST' or bool(initial_serial)

    if should_check and form.is_valid():
        serial = form.cleaned_data['serial_number']
        product = ProductWarranty.objects.filter(serial_number__iexact=serial).first()
        if product:
            result = get_public_status(product)
        else:
            not_found_serial = serial
            result = {
                'kind': 'danger',
                'title': 'Серийный номер не найден',
                'message': 'Проверьте правильность ввода или свяжитесь с официальной поддержкой.',
            }

    return render(request, 'warranty/check.html', {
        'form': form,
        'product': product,
        'result': result,
        'not_found_serial': not_found_serial,
        # ВАЖНО: замените номер ниже на ваш реальный номер поддержки.
        # Формат для WhatsApp: только цифры, без +, пробелов и скобок.
        'support_whatsapp_number': '77058157553',
        'support_phone_display': '+7 705 815 75 53',
    })
