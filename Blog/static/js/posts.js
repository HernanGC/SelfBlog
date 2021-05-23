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
    toggleDisplay(loadingImg, initialDisplayBtn);
    getRequest(`/get-posts?current=${currentPosts}`, {'X-CSRFToken': getCookie()})
        .then(data => {
            if (data['posts']) {
                for (let post of data['posts']) {
                    createPostElement(post.id, post.title, post.content, 'Hernan G', post.created_at);
                }
            }
            console.log(data);
        })
}

const createPostElement = function (id, title, content, author, creationDate) {
    let post = `<div class="blog-post card" onclick="window.location.href='/post/${id}'">
                    <h4>${title}</h4>
                    <p>${content}</p>
                    <span>${author}</span>
                    <span>${creationDate}</span>
                </div>`;
    parentDiv.appendChild(post);
}

morePostsButton.addEventListener('click', getMorePosts);