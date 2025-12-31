window.addEventListener('pywebviewready', async () => {
  console.log("init() called");
  const users = await window.pywebview.api.get_users();
  console.log(users);
  $("#userlist").html(users[0].name);
});

/*
*/

