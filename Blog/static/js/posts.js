import {getCookie, postRequest, getRequest, toggleDisplay} from './utils.js';

const morePostsButton = document.getElementById('see-more-btn');
const loadingImg = document.getElementById('loading-img');
const parentDiv = document.getElementById('posts-container');
let initialPosts = 9;
let currentPosts = 9;

const getMorePosts = function () {
    console.log(morePostsButton);
    const initialDisplayBtn = morePostsButton.style.display;
    const initialDisplayImg = loadingImg.style.display;
    toggleDisplay(morePostsButton, 'none');
    toggleDisplay(loadingImg, 'initial');
    window.scrollTo(0,document.body.scrollHeight);
    setTimeout(function () {
        getRequest(`/get-posts?current=${currentPosts}`, {'X-CSRFToken': getCookie()})
        .then(data => {
            if (data['posts']) {
                currentPosts += data['posts'].length; 
                for (let post of data['posts']) {
                    createPostElement(post.id, post.title, post.content, 'Hernan G', post.created_at);
                }
            }
            toggleDisplay(morePostsButton, 'initial');
            toggleDisplay(loadingImg, 'none');
            console.log(data);
        })
    }, 1000);
    
}

const createPostElement = function (id, title, content, author, creationDate) {
    let divEl = document.createElement('div');
    divEl.setAttribute('class', 'blog-post card');
    divEl.setAttribute('onclick', `window.location.href='/post/${id}'`);

    let hfourEl = document.createElement('h4');
    hfourEl.appendChild(document.createTextNode(title));

    let pEl = document.createElement('p');
    pEl.appendChild(document.createTextNode(content));

    let spanEl = document.createElement('span');
    spanEl.appendChild(document.createTextNode(author));

    let spanElTwo = document.createElement('span');
    spanElTwo.appendChild(document.createTextNode(creationDate));

    divEl.appendChild(hfourEl);
    divEl.appendChild(pEl);
    divEl.appendChild(spanEl);
    divEl.appendChild(spanElTwo);

    parentDiv.appendChild(divEl);
}

morePostsButton.addEventListener('click', getMorePosts);