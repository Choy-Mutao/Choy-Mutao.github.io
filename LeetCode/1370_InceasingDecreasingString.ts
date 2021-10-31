function sortString(s: string): string {
    let result = [];
    const strArray = Array.from(s);
    do {
        // 1. 升序排序
        strArray.sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0));
        // 去重
        for (var i = 1; i < strArray.length + 1; i++) {
            if (strArray[i - 1] !== strArray[i]) {
                result.push(...strArray.splice(i - 1, 1));
            }
        }
        // 2. 降序排序
        strArray.sort((a, b) => b.charCodeAt(0) - a.charCodeAt(0));
        // 去重
        for (var i = 1; i < strArray.length + 1; i++) {
            if (strArray[i - 1] !== strArray[i]) {
                result .push(...strArray.splice(i - 1, 1));
            }
        }
    } while (strArray.length > 0)
    return result.join('');
};

var result = sortString('aaabbfbccczxvhaasdrqeqeeqrddyqereee');
console.log(result);

function sort(s: string): string {
    const num = new Array(26).fill(0);
    for (let ch of s) {
        num[ch.charCodeAt(0) - 'a'.charCodeAt(0)]++;
    }
    let ret = '';
    while (ret.length < s.length) {
        for (let i = 0; i < 26; i++) {
            if (num[i]) {
                ret += String.fromCharCode(i + 'a'.charCodeAt(0));
                num[i]--;
            }
        }
        for (let i = 25; i >= 0; i--) {
            if (num[i]) {
                ret += String.fromCharCode(i + 'a'.charCodeAt(0));
                num[i]--;
            }
        }
    }
    return ret;
}