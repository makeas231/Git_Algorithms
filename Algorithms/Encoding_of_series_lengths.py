'''Модуль выполняет кодирование и раскадирование серий'''

def series_encoding(series: str):
    """Кодировка серий"""
    list_encoding_series = []
    count = 0
    value = None
    for i in series:
        if i == value or not value:
            count += 1
        else:
            list_encoding_series.append(str(count))
            list_encoding_series.append(value)
            count = 1
        value = i
    if count:
        list_encoding_series.append(str(count))
        list_encoding_series.append(value)
        
    return "".join(list_encoding_series)
    
def decoding(series: str):
    """Раскадировкa серий"""
    list_decoding_series = []
    index = 0
    while index < len(series):
        list_decoding_series.append(int(series[index]) * series[index + 1])
        index += 2
        
    return ''.join(list_decoding_series)