/*
*
* 工具类
*
*/

var host = "http://127.0.0.1:10010";  //域名

function http(url, data, method, success, fail) {
    /**
     * http请求方法封装（ajax）
     * @param url
     * @param data
     * @param method
     * @param success
     * @param fail
     */

    var data = method == 'GET' ? data : JSON.stringify(data);

    $.ajax({
        type: method,
        contentType: "application/json; charset=utf-8",
        data: data,  //请求参数
        url: url,
        dataType: 'json',
        success: success,  //成功回调
        fail: fail  //失败回调
    });

}


String.prototype.format = function () {
    /**
     * format 函数（方便动态渲染）
     * var str = "js实现用{two}自符串替换占位符{two} {three}  {one} ".format({one: "I",two: "LOVE",three: "YOU"});
     * var str2 = "js实现用{1}自符串替换占位符{1} {2}  {0} ".format("I","LOVE","YOU");
     */
    if (arguments.length == 0) return this;
    var param = arguments[0];
    var s = this;
    if (typeof (param) == 'object') {
        for (var key in param)
            s = s.replace(new RegExp("\\{" + key + "\\}", "g"), param[key]);
        return s;
    } else {
        for (var i = 0; i < arguments.length; i++)
            s = s.replace(new RegExp("\\{" + i + "\\}", "g"), arguments[i]);
        return s;
    }
};

function getFormatDate(data){
    /**
     * 格式化时间
     * @type {Date}
     */

    var nowDate = new Date(data);
    var year = nowDate.getFullYear();
    var month = nowDate.getMonth() + 1 < 10 ? "0" + (nowDate.getMonth() + 1) : nowDate.getMonth() + 1;
    var date = nowDate.getDate() < 10 ? "0" + nowDate.getDate() : nowDate.getDate();
    var hour = nowDate.getHours()< 10 ? "0" + nowDate.getHours() : nowDate.getHours();
    var minute = nowDate.getMinutes()< 10 ? "0" + nowDate.getMinutes() : nowDate.getMinutes();
    var second = nowDate.getSeconds()< 10 ? "0" + nowDate.getSeconds() : nowDate.getSeconds();

    return year + "-" + month + "-" + date+" "+hour+":"+minute+":"+second;
}
