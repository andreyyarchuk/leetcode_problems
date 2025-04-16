function canConstruct(ransomNote: string, magazine: string): boolean {
    // Преобразуем строку magazine в массив символов
    const magazineArr = magazine.split('');
    
    // Перебираем все буквы ransomNote
    for (let i = 0; i < ransomNote.length; i++) {
        const letter = ransomNote[i];
        const index = magazineArr.indexOf(letter); // Находим индекс буквы в magazineArr
        
        // Если буква не найдена или её больше нет в magazineArr — возвращаем false
        if (index === -1) {
            return false;
        }
        
        // Убираем использованную букву из magazineArr
        magazineArr.splice(index, 1);
    }
    
    // Если все буквы ransomNote были использованы — возвращаем true
    return true;
}
