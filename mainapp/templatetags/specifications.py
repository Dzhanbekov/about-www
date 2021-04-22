# from django import template
# from django.utils.safestring import mark_safe
# from mainapp.models import Smartphone
#
# register = template.Library()
#
# TABLE_HAD = """
#                 <table class="table">
#                 <tbody>
#             """
#
# TABLE_TAIL = """
#                 </tbody>
#                 </table>
#
#             """
# TABLE_CONTENT = """
#                 <tr>
#                     <td>{name}</td>
#                     <td>{value}</td>
#                 </tr>
#
#                 """
#
# PRODUCT_SPEC = {
#     'notebook': {
#         'Диагональ': 'diagonal',
#         'Тип Дисплея': 'display_type',
#         'Частота процессора': 'processor_freq',
#         'Оперативная память': 'ran',
#         'Видеокарта': 'video',
#         'Аккумулятор': 'time_without_charge',
#     },
#     'smartphone': {
#                     'Диагональ': 'diagonal',
#                     'Тип Дисплея': 'display_type',
#                     'Разрешение экрана': 'resolution',
#                     'объем батареи': 'accum_volume',
#                     'Оперативная память': 'ran',
#                     'Наличие карты памяти': 'sd',
#                     'максимальный объем встроенной памяти': 'sd_valume_max',
#                     'Главная камера (MP)': 'main_cam_ap',
#                     'фронтальная камерa (MP)': 'front_cam_ap',
# }
# }
#
# def get_product_spec(product, model_name):
#     table_content = ''
#     for name, value in product_spec[model_name].items():
#         table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
#     return table_content
#
#
# @register.filter
# def product_spec(product):
#     model_name = product.__class__.meta.model.name
#     if isinstance(product, Smartphone):
#         if not product.sd:
#             PRODUCT_SPEC['smartphone'].pop('максимальный объем встроенной памяти')
#         else:
#             PRODUCT_SPEC['smartphone']['максимальный объем встроенной памяти'] = 'sd_volume_max'
#
#     return mark_safe(TABLE_HAD + get_product_spec(product, model_name) + TABLE_TAIL)