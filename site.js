/* 流入元の記録: 最初に着地したときの参照元(ホスト名のみ)と utm_source を
   タブを閉じるまで保持し、お問い合わせフォームの hidden 欄「流入元」に入れる。
   Cookie は使わない。個人を識別する情報は扱わない。 */
(function () {
  var KEY = 'fukuya_source';
  function read() { try { return sessionStorage.getItem(KEY); } catch (e) { return null; } }
  function write(v) { try { sessionStorage.setItem(KEY, v); } catch (e) {} }

  var value = read();
  if (!value) {
    var utm = '';
    try { utm = (new URLSearchParams(location.search).get('utm_source') || '').replace(/[^\w.\-]/g, '').slice(0, 60); } catch (e) {}
    var ref = '';
    try {
      if (document.referrer) {
        var host = new URL(document.referrer).hostname;
        if (host && host !== location.hostname) ref = host;
      }
    } catch (e) {}
    var parts = [];
    if (utm) parts.push('utm_source=' + utm);
    if (ref) parts.push('参照元=' + ref);
    if (!parts.length) parts.push('直接アクセスまたは不明');
    parts.push('最初のページ=' + location.pathname);
    value = parts.join(' / ');
    write(value);
  }
  var field = document.querySelector('input[name="流入元"]');
  if (field) field.value = value;
})();
