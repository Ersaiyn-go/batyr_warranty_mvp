from django.shortcuts import render

from .forms import WarrantyCheckForm
from .models import ProductWarranty


TEXTS = {
    'kk': {
        'page_title': 'Batyr Watch кепілдігін тексеру',
        'brand_subtitle': 'Ресми кепілдік тексерісі',
        'header_support': 'Ресми қолдау',

        'badge': 'Ресми тексеру',
        'hero_title': 'Batyr Watch сағатыңыздың түпнұсқалығын тексеріңіз',
        'subtitle': 'Сериялық нөмірді енгізіңіз: жүйе тауардың статусын, моделін және кепілдік мерзімін көрсетеді.',
        'serial_label': 'Сериялық нөмір',
        'serial_placeholder': 'Мысалы: BRSP390001',
        'button_check': 'Тексеру',

        'info_title': 'Жүйе нені көрсетеді?',
        'info_1': 'Тауардың түпнұсқалығы',
        'info_2': 'Құрылғы моделі мен түсі',
        'info_3': 'Кепілдік статусы',
        'info_4': 'Кепілдіктің аяқталу күні',

        'in_stock_title': 'Тауар түпнұсқа, бірақ кепілдік әлі іске қосылмаған',
        'in_stock_message': 'Сериялық нөмір ресми базада бар. Кепілдік сатылымнан және активациядан кейін басталады.',

        'sold_active_title': 'Тауар түпнұсқа. Кепілдік белсенді',
        'sold_active_message': 'Кепілдіктің аяқталуына {days} күн қалды.',

        'expired_title': 'Тауар түпнұсқа, бірақ кепілдік мерзімі аяқталған',
        'expired_message': 'Бұл сериялық нөмір бойынша ресми кепілдік мерзімі аяқталды.',

        'returned_title': 'Сериялық нөмір табылды, бірақ тауар қайтарылған ретінде белгіленген',
        'returned_message': 'Статусты нақтылау үшін қолдау қызметіне хабарласыңыз.',

        'replaced_title': 'Сериялық нөмір табылды, бірақ тауар ауыстырылған',
        'replaced_message': 'Жаңа құрылғыны тексеру үшін қолдау қызметіне хабарласыңыз.',

        'manual_title': 'Сериялық нөмір қосымша тексеруді қажет етеді',
        'manual_message': 'Тауарды қолмен тексеру үшін қолдау қызметіне хабарласыңыз.',

        'not_found_title': 'Сериялық нөмір табылмады',
        'not_found_message': 'Нөмірдің дұрыс жазылғанын тексеріңіз немесе ресми қолдау қызметіне хабарласыңыз.',

        'detail_serial': 'Сериялық нөмір',
        'detail_model': 'Модель',
        'detail_color': 'Түс',
        'detail_sale_date': 'Сату күні',
        'detail_warranty_until': 'Кепілдік мерзімі',
        'detail_buyer': 'Сатып алушы',
        'detail_entered_serial': 'Енгізілген нөмір',
        'not_displayed': 'Көрсетілмейді',

        'whatsapp_button': 'Кепілдік бойынша қолдау алу',
        'whatsapp_message': 'Сәлеметсіз бе! Кепілдік бойынша қолдау алғым келеді.',
        'support_number': 'Қолдау нөмірі',

        'footer_text': 'Тауардың түпнұсқалығын және кепілдік мерзімін ресми тексеру.',
        'footer_managers': 'Менеджерлер',
        'footer_sales': 'Сату',
        'footer_warranty': 'Кепілдік',
        'footer_service': 'Сервис',
        'footer_socials': 'Әлеуметтік желілер',
        'footer_rights': 'Барлық құқықтар қорғалған.',
        'footer_privacy': 'Ашық бет клиенттің толық жеке деректерін көрсетпейді.',
    },

    'ru': {
        'page_title': 'Проверка гарантии Batyr Watch',
        'brand_subtitle': 'Official warranty check',
        'header_support': 'Официальная поддержка',

        'badge': 'Официальная проверка',
        'hero_title': 'Проверьте оригинальность вашего Batyr Watch',
        'subtitle': 'Введите серийный номер устройства, чтобы узнать статус товара, модель и срок действия гарантии.',
        'serial_label': 'Серийный номер',
        'serial_placeholder': 'Например: BRSP390001',
        'button_check': 'Проверить',

        'info_title': 'Что показывает система?',
        'info_1': 'Оригинальность товара',
        'info_2': 'Модель и цвет устройства',
        'info_3': 'Статус гарантии',
        'info_4': 'Дата окончания гарантии',

        'in_stock_title': 'Товар оригинальный, но гарантия ещё не активирована',
        'in_stock_message': 'Серийный номер есть в официальной базе. Гарантия начнётся после продажи и активации.',

        'sold_active_title': 'Товар оригинальный. Гарантия активна',
        'sold_active_message': 'До окончания гарантии осталось {days} дней.',

        'expired_title': 'Товар оригинальный, но гарантия истекла',
        'expired_message': 'Срок официальной гарантии по этому серийному номеру завершён.',

        'returned_title': 'Серийный номер найден, но товар отмечен как возврат',
        'returned_message': 'Для уточнения статуса обратитесь в поддержку.',

        'replaced_title': 'Серийный номер найден, но товар был заменён',
        'replaced_message': 'Для проверки нового устройства обратитесь в поддержку.',

        'manual_title': 'Серийный номер требует проверки',
        'manual_message': 'Обратитесь в поддержку для ручной проверки товара.',

        'not_found_title': 'Серийный номер не найден',
        'not_found_message': 'Проверьте правильность ввода или свяжитесь с официальной поддержкой.',

        'detail_serial': 'Серийный номер',
        'detail_model': 'Модель',
        'detail_color': 'Цвет',
        'detail_sale_date': 'Дата продажи',
        'detail_warranty_until': 'Гарантия до',
        'detail_buyer': 'Покупатель',
        'detail_entered_serial': 'Введённый номер',
        'not_displayed': 'Не отображается',

        'whatsapp_button': 'Получить поддержку по гарантии',
        'whatsapp_message': 'Здравствуйте! Хочу получить поддержку по гарантии.',
        'support_number': 'Номер поддержки',

        'footer_text': 'Официальная проверка оригинальности товара и срока гарантии.',
        'footer_managers': 'Менеджеры',
        'footer_sales': 'Продажи',
        'footer_warranty': 'Гарантия',
        'footer_service': 'Сервис',
        'footer_socials': 'Социальные сети',
        'footer_rights': 'Все права защищены.',
        'footer_privacy': 'Публичная страница не показывает полные личные данные покупателя.',
    }
}


def get_site_language(request):
    selected_lang = request.GET.get('lang') or request.POST.get('lang')

    if selected_lang in TEXTS:
        request.session['site_lang'] = selected_lang
        return selected_lang

    saved_lang = request.session.get('site_lang')

    if saved_lang in TEXTS:
        return saved_lang

    return 'kk'


def apply_form_language(form, t):
    form.fields['serial_number'].label = t['serial_label']
    form.fields['serial_number'].widget.attrs['placeholder'] = t['serial_placeholder']


def get_display_color(color, lang):
    if not color:
        return ''

    color = color.strip()

    if lang == 'kk':
        color_map = {
            'Черный': 'Қара',
            'Чёрный': 'Қара',
            'Серый': 'Сұр',
            'Бежевый': 'Бежевый',
            'Титан': 'Титан',
        }

        return color_map.get(color, color)

    return color


def get_public_status(product: ProductWarranty, t):
    if product.status == ProductWarranty.Status.IN_STOCK:
        return {
            'kind': 'info',
            'title': t['in_stock_title'],
            'message': t['in_stock_message'],
        }

    if product.status == ProductWarranty.Status.SOLD:
        if product.is_warranty_active:
            return {
                'kind': 'success',
                'title': t['sold_active_title'],
                'message': t['sold_active_message'].format(days=product.days_left),
            }

        return {
            'kind': 'warning',
            'title': t['expired_title'],
            'message': t['expired_message'],
        }

    if product.status == ProductWarranty.Status.RETURNED:
        return {
            'kind': 'warning',
            'title': t['returned_title'],
            'message': t['returned_message'],
        }

    if product.status == ProductWarranty.Status.REPLACED:
        return {
            'kind': 'warning',
            'title': t['replaced_title'],
            'message': t['replaced_message'],
        }

    return {
        'kind': 'danger',
        'title': t['manual_title'],
        'message': t['manual_message'],
    }


def check_warranty(request):
    lang = get_site_language(request)
    t = TEXTS[lang]

    result = None
    product = None
    not_found_serial = None
    display_color = ''

    serial_from_url = request.GET.get('serial', '').strip()
    current_serial = serial_from_url

    if request.method == 'POST':
        form = WarrantyCheckForm(request.POST)
        current_serial = request.POST.get('serial_number', '').strip()
        should_check = True

    elif serial_from_url:
        form = WarrantyCheckForm({'serial_number': serial_from_url})
        should_check = True

    else:
        form = WarrantyCheckForm()
        should_check = False

    apply_form_language(form, t)

    if should_check and form.is_valid():
        serial = form.cleaned_data['serial_number'].strip().upper()
        current_serial = serial

        product = ProductWarranty.objects.filter(
            serial_number__iexact=serial
        ).first()

        if product:
            result = get_public_status(product, t)
            display_color = get_display_color(product.color, lang)
        else:
            not_found_serial = serial
            result = {
                'kind': 'danger',
                'title': t['not_found_title'],
                'message': t['not_found_message'],
            }

    return render(request, 'warranty/check.html', {
        'form': form,
        'product': product,
        'result': result,
        'not_found_serial': not_found_serial,
        'display_color': display_color,
        'support_whatsapp_number': '77058157553',
        'support_phone_display': '+7 705 815 75 53',
        'lang': lang,
        't': t,
        'current_serial': current_serial,
    })