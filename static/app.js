async function tweet() {
  // by default its a GET
  const connection = await fetch("/tweet") //connection sometimes shortened to conn
  const dataFromServer = await connection.text()
  console.log(dataFromServer)

  document.querySelector("#message").innerHTML = dataFromServer
}

async function save() {
  // if other methodes (anything but GET) are needed, use the second argument
  console.log(event) // click
  console.log(event.target) // button
  console.log(event.target.form) // form

  const theForm = event.target.form
  const connection = await fetch("/save", {
    method : "POST",
    body : new FormData(theForm)

  })
  const dataFromServer = await connection.json()
  console.log(dataFromServer)

  // document.querySelector("#user").innerHTML = dataFromServer
  document.querySelector("#user").innerHTML = `Hi, ${dataFromServer.user_name} ${dataFromServer.user_last_name}, your nickname is ${dataFromServer.user_nick_name}`

}

// conn = connection
// data = dataFromServer
async function likeTweet() {
  console.log("like tweet")
  const conn = await fetch("/api-like-tweet")
  if(conn.ok) {
    const data = await conn.json()
    document.querySelector("#like_tweet").classList.toggle("hidden")
    document.querySelector("#unlike_tweet").classList.toggle("hidden")
  } else {
    console.log("error")
  }
}

async function unlikeTweet() {
  console.log("like tweet")
  const conn = await fetch("/api-unlike-tweet")
  if(conn.ok) {
    const data = await conn.json()
    document.querySelector("#like_tweet").classList.toggle("hidden")
    document.querySelector("#unlike_tweet").classList.toggle("hidden")
  } else {
    console.log("error")
  }
}
/*
const burger = document.querySelector(".burger");
const nav = document.querySelector("nav");

burger.addEventListener("click", () => {
  // toggle nav
  nav.classList.toggle("active");

  // toggle icon
  burger.classList.toggle("open");
});
*/