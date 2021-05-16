import Element from './Element.js';

class FormModal {

    constructor() {
        this.formData = {
            type: 'p',
            attributes: {
                'class': 'test'
            },
            children: 'test'
        }
        this.formModal = {
            type: 'div',
            parent: document.body,
            attributes: {
                'class': 'modal-form-container'
            },
            children: this.formData
        }
    }

    createBlog() {
        let formModal = new Element(this.formModal);
        return formModal;
    }

    createOverlay() {

    }
}

export default FormModal;

let formModal = new FormModal();