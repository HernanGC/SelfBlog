export const postRequest = async (url, headers, body = {}) => {
    const response = await fetch(url, {
        method: 'POST',
        headers: headers,
        body: body
    });
    return response.json();
}

export const getRequest = async (url, headers) => {
    const response = await fetch(url, {
        headers: headers,
    });
    return response.json();
}

export const getCookie = function (csrfCookie = 'csrftoken') {
    let cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        let cookieMatch = cookie.split('=')[0].trim();
        if (cookieMatch === csrfCookie) {
            return cookieMatch;
        }
    }
    return false;
}

export const toggleDisplay = function (element, display) {
    element.style.display = display;
}
