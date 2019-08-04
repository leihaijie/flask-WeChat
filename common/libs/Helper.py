from flask import g, render_template
import datetime
"""
统一渲染方法
"""
def ops_render(template, context={}):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template,**context)


'''
自定义分页类
'''
def iPagination(params):
    import math

    ret = {
        "is_prev": 1,  # 上一页
        "is_next": 1,  # 下一页
        "from": 0,     # 开始
        "end": 0,      # 结束
        "current": 0,  #当前
        "total_pages": 0,  # 总共页数
        "page_size" : 0,   # 每页大小
        "total" : 0,       # 总共记录数
        "url": params['url']   # url地址
    }

    total = int( params['total'] )
    page_size = int( params['page_size'] )
    page = int( params['page'] )
    display = int( params['display'] )
    total_pages = int( math.ceil( total / page_size ) )
    total_pages = total_pages if total_pages > 0 else 1
    if page <= 1:
        ret['is_prev'] = 0

    if page >= total_pages:
        ret['is_next'] = 0

    semi = int( math.ceil( display / 2 ) )

    if page - semi > 0 :
        ret['from'] = page - semi
    else:
        ret['from'] = 1

    if page + semi <= total_pages :
        ret['end'] = page + semi
    else:
        ret['end'] = total_pages

    ret['current'] = page
    ret['total_pages'] = total_pages
    ret['page_size'] = page_size
    ret['total'] = total
    ret['range'] = range( ret['from'],ret['end'] + 1 )
    return ret


"""
获取当前时间
"""
def getCurrentDate(format="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.now().strftime(format)


'''
获取格式化的时间
'''
def getFormatDate( date = None ,format = "%Y-%m-%d %H:%M:%S" ):
    if date is None:
        date = datetime.datetime.now()

    return date.strftime( format )


"""
从obj中取出想要的数据
"""
def selectFilterObj(obj, field):
    ret = []
    for item in obj:
        if not hasattr(item, field ):
            break
        if getattr(item, field) in ret:
            continue
        ret.append(getattr(item, field))
    return ret


"""
根据某个字段获取一个dict出来
"""
def getDictFilterField(db_model, select_filed, key_field, id_list):
    ret = {}
    query = db_model.query
    if id_list and len(id_list) > 0:
        query = query.filter(select_filed.in_(id_list))

    list = query.all()
    if not list:
        return ret
    for item in list:
        if not hasattr(item, key_field):
            break

        ret[getattr(item, key_field)] = item
    return ret



def getDictListFilterField( db_model,select_filed,key_field,id_list ):
    ret = {}
    query = db_model.query
    if id_list and len( id_list ) > 0:
        query = query.filter( select_filed.in_( id_list ) )

    list = query.all()
    if not list:
        return ret
    for item in list:
        if not hasattr( item,key_field ):
            break
        if getattr( item,key_field ) not in ret:
            ret[getattr(item, key_field)] = []

        ret[ getattr( item,key_field ) ].append(item )
    return ret