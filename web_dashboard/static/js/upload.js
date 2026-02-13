document.getElementById('uploadForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById('fileInput');
    if (!fileInput.files[0]) return;

    const resultsCard = document.getElementById('resultsCard');
    const summaryResult = document.getElementById('summaryResult');
    const loader = document.getElementById('loader');
    const btn = document.getElementById('btnSummarize');

    // UI Feedback
    resultsCard.style.display = 'block';
    summaryResult.innerHTML = '';
    loader.style.display = 'block';
    btn.disabled = true;
    btn.innerText = 'Procesando con Llama 3.1...';

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    try {
        const response = await fetch('/summarize', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.error) {
            summaryResult.innerHTML = `<span style="color: #f85149;">Error: ${data.error}</span>`;
        } else {
            summaryResult.innerText = data.summary;
        }
    } catch (err) {
        summaryResult.innerHTML = `<span style="color: #f85149;">Error de conexión con el servidor.</span>`;
    } finally {
        loader.style.display = 'none';
        btn.disabled = false;
        btn.innerText = 'Generar Resumen';
    }
});

// Drop Zone Interactivity
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');

dropZone.addEventListener('click', () => fileInput.click());

fileInput.addEventListener('change', () => {
    if (fileInput.files.length) {
        updateThumbnail(dropZone, fileInput.files[0]);
    }
});

dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('drop-zone--over');
});

['dragleave', 'dragend'].forEach(type => {
    dropZone.addEventListener(type, () => {
        dropZone.classList.remove('drop-zone--over');
    });
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();

    if (e.dataTransfer.files.length) {
        fileInput.files = e.dataTransfer.files;
        updateThumbnail(dropZone, e.dataTransfer.files[0]);
    }

    dropZone.classList.remove('drop-zone--over');
});

function updateThumbnail(dropZone, file) {
    let thumbnailElement = dropZone.querySelector('.drop-zone__thumb');

    if (dropZone.querySelector('.drop-zone__prompt')) {
        dropZone.querySelector('.drop-zone__prompt').remove();
    }

    if (!thumbnailElement) {
        thumbnailElement = document.createElement('div');
        thumbnailElement.classList.add('drop-zone__thumb');
        dropZone.appendChild(thumbnailElement);
    }

    thumbnailElement.dataset.label = file.name;
    thumbnailElement.innerText = `Archivo seleccionado: ${file.name}`;
}
