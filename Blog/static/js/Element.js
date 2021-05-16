class Element {
    constructor(type, parent, attributes, children) {
        this.createElement(type, parent, attributes = {}, children = []);
    }

    createElement({
        type,
        parent,
        attributes,
        children
    }) {
        const element = document.createElement(type);

        Object.keys(attributes).forEach(key => {
            element.setAttribute(key, attributes[key]);
        });

        children.forEach(child => {
            if (typeof child == 'object') {
                return this.createElement({...child, parent: element});
            }
            const textNode = document.createTextNode(child);
            element.appendChild(textNode);
        });

        parent.appendChild(element);
        return element;
    }
}

export default Element;