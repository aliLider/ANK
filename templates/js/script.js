var m = {  
    'select category': 'Пожалуйста, выберите категорию',
    'No files found for matching criteria': 'файл не найден',
    
};

function getCurrentLanguage() {
    return document.getElementById('current_language_code').value;
}

function getLangText(text) {
    if (getCurrentLanguage() == 'ja') {
        return m[text];
    }
    return text;
}


document.getElementById('file_msg').innerHTML = getLangText('No files found for matching criteria');
