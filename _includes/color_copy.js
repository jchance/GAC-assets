function copyToClipboard(text, element) {
  navigator.clipboard.writeText(text).then(() => {
    const btn = element;
    const originalHTML = btn.innerHTML;
    const originalStyle = btn.getAttribute('style');
    const copiedColor = btn.dataset.copiedColor || '#2BB3B1';
    btn.innerHTML = btn.dataset.copiedIcon + ' Copied!';
    btn.style.backgroundColor = copiedColor;
    btn.style.color = 'white';
    btn.style.border = 'none';
    setTimeout(() => {
      btn.innerHTML = originalHTML;
      btn.setAttribute('style', originalStyle);
    }, 2000);
  }).catch(() => {
    alert('Failed to copy');
  });
}
