console.log('hello world');
// When you add the document to console.log you can see the whole html in console. adding a dot after the document will give you a list of all of kinds of things you can do with the document. Below we added the .URL and it shows the url address in the console.

console.log(document);

const test = document.getElementById('test');
console.log(test);

const posts2 = document.getElementById('posts2');
console.log(posts2);

const spinner = document.getElementById('spinner-box');

setTimeout(() => {
    test.textContent = "How ar you doing.";
}, 2000);

$.ajax({
    type: 'GET',
    url: '/posts-json/',
    success: function(response){
        // Remember this .data is from django views, it gives json string
        console.log(response.data)
        // Below turns JSON string into javascript objects, now you can add data to the DOM
        const data = JSON.parse(response.data)
        console.log(data)
        // Remember to use oop, ex el.fields.body
        setTimeout(() => {
            data.forEach(el => {
                posts2.innerHTML += `${el.fields.body}<br>`
            });
            // To spinner variable add class of 'not-visible'. This class was written in style.css. This will take off spinner after 2 seconds
            spinner.classList.add('not-visible')
        }, 2000)
        
    },
    error: function(error){
        console.log(error)
    }
});