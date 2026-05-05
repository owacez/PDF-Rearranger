from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import fitz
import os

app = Flask(__name__)
app.secret_key = 'pdf-rearranger'

UPLOAD_FOLDER = 'uploads'
PREVIEW_FOLDER = 'static/previews'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PREVIEW_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['pdf']
    if not file:
        flash('No file uploaded')
        return redirect(url_for('index'))

    pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(pdf_path)

    # Open PDF
    doc = fitz.open(pdf_path)

    image_paths = []

    # Convert pages to images
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=fitz.Matrix(0.3, 0.3))  # low-res thumbnail
        img_name = f"{file.filename}_page_{i}.png"
        img_path = os.path.join(PREVIEW_FOLDER, img_name)
        pix.save(img_path)

        image_paths.append(f"previews/{img_name}")

    return render_template(
        'rearrange.html',
        images=image_paths,
        filename=file.filename
    )


@app.route('/process', methods=['POST'])
def process():
    filename = request.form['filename']
    order = request.form['order']

    pdf_path = os.path.join(UPLOAD_FOLDER, filename)
    doc = fitz.open(pdf_path)

    new_doc = fitz.open()

    try:
        new_order = list(map(int, order.split(',')))

        for page_num in new_order:
            new_doc.insert_pdf(doc, from_page=page_num-1, to_page=page_num-1)

    except:
        flash('Invalid order')
        return redirect(url_for('index'))

    output_path = os.path.join(UPLOAD_FOLDER, 'output.pdf')
    new_doc.save(output_path)

    return send_file(output_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)