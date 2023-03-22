function previewPdf() {
  const fileInput = document.getElementById('pdf-file');
  const file = fileInput.files[0];
  const reader = new FileReader();

  reader.onload = function() {
    const pdfPreview = document.querySelector('.pdf-preview');
    const pdfObject = document.createElement('object');
    pdfObject.data = reader.result;
    pdfObject.type = 'application/pdf';
    pdfObject.width = '100%';
    pdfObject.height = '300px';
    pdfPreview.innerHTML = '';
    pdfPreview.appendChild(pdfObject);
  }

  reader.readAsDataURL(file);
}
