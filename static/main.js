console.log('hello world');
// When you add the document to console.log you can see the whole html in console. adding a dot after the document will give you a list of all of kinds of things you can do with the document. Below we added the .URL and it shows the url address in the console.

console.log(document);

const test = document.getElementById('test');
console.log(test);

setTimeout(() => {
    test.textContent = "How ar you doing.";
}, 2000);