const deletePost = (url, redirect) => {
    let cookie = getCookie();
    let areYouSure = window.confirm('Are you sure you want to delete this post?');
    if (areYouSure) {
        postRequest(url, {'X-CSRFToken': cookie})
            .then(data => {
                window.alert(data.message)
                if (data.success === 'true') {
                    window.location.href = redirect;
                }
        });
    }
    
}

const postRequest = async (url, headers) => {
    const response = await fetch(url, {
        method: 'POST',
        headers: headers
    });
    return response.json();
}

const getCookie = function (csrfCookie = 'csrftoken') {
    let cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        if (cookie.split('=')[0].trim() === csrfCookie) {
            return cookie.split('=')[1].trim();
        }
    }
    return false;
}