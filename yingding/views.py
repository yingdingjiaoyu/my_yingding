import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Admissions_data
from django.core.paginator import Paginator


op_to_lookup = {
    'equal': 'exact',
    'not_equal': 'exact',
    'like': 'contains',
    'not_like': 'contains',
    'starts_with': 'startswith',
    'ends_with': 'endswith',
    'less': 'lt',
    'less_or_equal': 'lte',
    'greater': 'gt',
    'greater_or_equal': 'gte',
    'between': 'range',
    'not_between': 'range',
    'select_equals': 'exact',
    'select_not_equals': 'exact',
    'select_any_in': 'in',
    'select_not_any_in': 'in',
}

def index(request):
    return render(request, 'yingding/index.html')

def tianbao(request):
    admissions_data_fields = [{'name':field.name, 'label':field.verbose_name} for field in Admissions_data._meta.fields]
    return render(request, 'yingding/tianbao.html', {'admissions_data_fields': admissions_data_fields})

def analyse_admissions_data_conditions(conditions):
    final_query = None
    for child in conditions['children']:
        model,field = child['left']['field'].split('.')
        lookup = op_to_lookup[child['op']]
        right = child['right']

        if model == 'admissions_data':
            params = {f'{field}__{lookup}': right}
        else:
            params = {f'{model}__{field}__{lookup}': right}

        if 'not_' in child['op']:
            child_query = Admissions_data.objects.exclude(**params)
        else:
            child_query = Admissions_data.objects.filter(**params)

        if final_query is None:
            final_query = child_query
        elif conditions['conjunction'] == 'and':
            final_query = final_query & child_query
        else:
            final_query = final_query | child_query
    return final_query

def admissions_data_filter_api(request):
    data = json.loads(request.body.decode())
    page = data.get('page', 1)
    per_page = data.get('perpage', 10)
    conditions = data.get('conditions',{})
    admissions_datas = analyse_admissions_data_conditions(conditions) if len(conditions) > 0 else Admissions_data.objects.all()
    admissions_datas = admissions_datas.order_by('-line_2021')

    paginator = Paginator(admissions_datas, per_page)
    page_obj = paginator.get_page(page)

    data = {
        'status': 0,
        'msg': 'ok',
        'data': {
            'total': admissions_datas.count(),
            'items': list(page_obj.object_list.values())
        }
    }
    return JsonResponse(data)