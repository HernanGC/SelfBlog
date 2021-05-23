import {getCookie, postRequest} from './utils.js';

const deleteButton = document.getElementById('delete-button');

// Functions
const deletePost = () => {
    console.log(deleteButton.dataset.delete);
    let cookie = getCookie();
    let areYouSure = window.confirm('Are you sure you want to delete this post?');
    if (areYouSure) {
        postRequest(deleteButton.dataset.delete, {'X-CSRFToken': cookie})
            .then(data => {
                window.alert(data.message)
                if (data.success === 'true') {
                    window.location.href = '/';
                }
        });
    }
}

deleteButton.addEventListener('click', deletePost);


