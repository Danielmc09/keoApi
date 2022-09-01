from .models import Stats

def validateStats(stats):
    """
    It takes a string as an argument, and returns a dictionary with the count of the string in the
    database, the total number of records in the database, and the ratio of the count to the total
    
    :param stats: The stats object that you want to validate
    :return: A dictionary with the count, total, and ratio of the stats.
    """
    result = Stats.objects.filter(result=stats).count()
    if result:
        total = Stats.objects.all().count()
        ratio = result/total
        queryset = {
            'count': result,
            'total': total,
            'ratio':round(ratio, 2)
        }
        return queryset
    return False