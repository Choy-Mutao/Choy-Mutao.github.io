function sortString(s) {
    var result = [];
    var strArray = Array.from(s);
    do {
        // 1. 升序排序
        strArray.sort(function (a, b) { return a.charCodeAt(0) - b.charCodeAt(0); });
        // 去重
        for (var i = 1; i < strArray.length + 1; i++) {
            if (strArray[i - 1] !== strArray[i]) {
                result.push.apply(result, strArray.splice(i - 1, 1));
            }
        }
        // 2. 降序排序
        strArray.sort(function (a, b) { return b.charCodeAt(0) - a.charCodeAt(0); });
        // 去重
        for (var i = 1; i < strArray.length + 1; i++) {
            if (strArray[i - 1] !== strArray[i]) {
                result.push.apply(result, strArray.splice(i - 1, 1));
            }
        }
    } while (strArray.length > 0);
    return result.join('');
}
;
var result = sortString('aaabbfbccczxvhaasdrqeqeeqrddyqereee');
console.log(result);
