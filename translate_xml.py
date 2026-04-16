import xml.etree.ElementTree as ET

translations = {
    "A copy of the result": "Копия результата",
    "The ticket representing the authentication result.": "Билет, представляющий результат аутентификации.",
    "The result.": "Результат.",
    "The failure exception.": "Исключение, указывающее на сбой.",
    "Additional state values for the authentication session.": "Дополнительные значения состояния для сеанса аутентификации.",
    "The failure message.": "Сообщение о сбое.",
    "The message that describes the error.": "Сообщение, описывающее ошибку.",
    "The <see cref=\"T:Microsoft.AspNetCore.Http.HttpContext\"/> context.": "Контекст <see cref=\"T:Microsoft.AspNetCore.Http.HttpContext\"/>.",
    "The name of the authentication scheme.": "Имя схемы аутентификации.",
    "The user.": "Пользователь.",
    "The task.": "Задача.",
    "The value of the token if present.": "Значение токена, если он присутствует.",
    "Configures the scheme.": "Настраивает схему.",
    "The name of the scheme being added.": "Имя добавляемой схемы.",
    "State values dictionary to use.": "Словарь значений состояния для использования.",
    "Parameters dictionary to use.": "Словарь параметров для использования.",
    "A copy.": "Копия.",
    "Property key.": "Ключ свойства.",
    "Retrieved value or <c>null</c> if the property is not set.": "Полученное значение или <c>null</c>, если свойство не установлено.",
    "Value to set or <see langword=\"null\" /> to remove the property.": "Значение для установки или <see langword=\"null\" /> для удаления свойства.",
    "Parameter type.": "Тип параметра.",
    "Parameter key.": "Ключ параметра.",
    "Retrieved value or the default value if the property is not set.": "Полученное значение или значение по умолчанию, если свойство не установлено.",
    "Value to set.": "Значение для установки.",
    "the <see cref=\"T:System.Security.Claims.ClaimsPrincipal\"/> that represents the authenticated user.": "<see cref=\"T:System.Security.Claims.ClaimsPrincipal\"/>, представляющий аутентифицированного пользователя.",
    "additional properties that can be consumed by the user or runtime.": "дополнительные свойства, которые могут быть использованы пользователем или средой выполнения.",
    "the authentication scheme that was responsible for this ticket.": "схема аутентификации, которая отвечала за этот билет.",
    "A copy of the ticket": "Копия билета",
    "The handler instance.": "Экземпляр обработчика.",
    "The name of the authentication scheme being handled.": "Имя обрабатываемой схемы аутентификации.",
    "<see langword=\"true\" /> if request processing should stop.": "<see langword=\"true\" />, если обработка запроса должна быть остановлена.",
    "All currently registered <see cref=\"T:Microsoft.AspNetCore.Authentication.AuthenticationScheme\"/>s.": "Все зарегистрированные <see cref=\"T:Microsoft.AspNetCore.Authentication.AuthenticationScheme\"/>.",
    "The name of the authenticationScheme.": "Имя схемы аутентификации.",
    "The scheme or null if not found.": "Схема или null, если не найдено.",
    "The scheme.": "Схема.",
    "true if the scheme was added successfully.": "true, если схема была успешно добавлена.",
    "The name of the authenticationScheme being removed.": "Имя удаляемой схемы аутентификации.",
    "The schemes in priority order for request handling": "Схемы в порядке приоритета для обработки запросов",
    "Unable to find the required '{0}' service. Please add all the required services by calling '{1}.{2}' in the application startup code.": "Не удалось найти требуемую службу '{0}'. Пожалуйста, добавьте все требуемые службы, вызвав '{1}.{2}' в коде запуска приложения.",
}

def translate_text(text):
    if not text or not text.strip():
        return text
    stripped = text.strip()
    if stripped in translations:
        leading = len(text) - len(text.lstrip())
        trailing = len(text) - len(text.rstrip())
        return ' ' * leading + translations[stripped] + ' ' * trailing
    return text

def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for eng, rus in translations.items():
        content = content.replace(eng, rus)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

process_file('/workspace/XML/Microsoft.AspNetCore.Authentication.Abstractions.xml', 
             '/workspace/Перевод/Microsoft.AspNetCore.Authentication.Abstractions.xml')
print("Готово!")
