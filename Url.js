var ch = request('ch');
var p = 1;
var f = 50;
if (ch.indexOf('-') > 0) {
	p = parseInt(ch.split('-')[1]);
	ch = ch.split('-')[0];
}
if (ch == '') ch = 1;
else ch = parseInt(ch);
var pi = '';
var ni = '';
var c = '';
var ci = 0;
var ps = '';
function ge(e) {
	return document.getElementById(e);
}
function ss(a, b, c, d) {
	var e = a.substring(b, b + c);
	return d == null ? e.replace(/[a-z]*/gi, "") : e;
}
function si(c) {
	ge('TheImg').src = 'http://img' + ss(c, 4, 2) + '.8comic.com/' + ss(c, 6, 1) + '/' + ti + '/' + ss(c, 0, 4) + '/' + nn(p) + '_' + ss(c, mm(p) + 10, 3, f) + '.jpg';
}
function nn(n) {
	return n < 10 ? '00' + n: n < 100 ? '0' + n: n;
}
function mm(p) {
	return (parseInt((p - 1) / 10) % 10) + (((p - 1) % 10) * 3)
};
function sp() {
	var cc = cs.length;
	for (var i = 0; i < cc / f; i++) {
		if (ss(cs, i * f, 4) == ch) {
			c = ss(cs, i * f, f, f);
			ci = i;
			break;
		}
	}
	if (c == '') {
		c = ss(cs, cc - f, f);
		ch = chs;
	}
	si(c);
	pi = ci > 0 ? ss(cs, ci * f - f, 4) : ch;
	var pt = '[ ' + pi + ' ]';
	ni = ci < cc - 1 ? ss(cs, ci * f + f, 4) : ch;
	var nt = '[ ' + ni + ' ]';
	ps = ss(c, 7, 3);
	initpage(ps, p, "pageindex");
	ge("lastchapter").innerHTML = ch;
	if (p > ps) {
		ge('next').style.display = 'none';
		ge('next2').style.display = 'none;';
	}
	if (p <= 1) {
		ge('prev').style.display = 'none;';
		ge('prev2').style.display = 'none;';
	}
	if (ch >= chs) ge('nextvol').style.display = "none";
	ge('nextname').innerHTML = nt;
	ge('prevname').innerHTML = pt;
	ge('pagenum').innerHTML = '\u7b2c' + p + '/' + ps + '\u9801';
}
function jn() {
	if (p < ps) j(p + 1);
	else alert('\u5df2\u7d93\u662f\u6700\u5f8c\u4e00\u9801\u4e86');
}
function jp() {
	if (p > 1) j(p - 1);
}
function nv() {
	if (ch < chs) jv(ni);
}
function pv() {
	if (ch > 1) jv(pi);
}
function lv() {
	jv(chs);
}
function j(n) {
	document.location.href = replaceurl("ch", ch + "-" + n);
}
function jv(n) {
	document.location.href = replaceurl("ch", n);
}