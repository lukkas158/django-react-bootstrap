import "./App.css";

import GoogleLogin from "react-google-login";
// or

function App() {
  function responseGoogle(response) {
    console.log(response);
  }
  return (
    <div className="App">
      <GoogleLogin
        clientId="731503379118-inahlhp2uvbidiactobo33t8obpo0638.apps.googleusercontent.com"
        buttonText="Login"
        onSuccess={responseGoogle}
        onFailure={responseGoogle}
      />
      ,
    </div>
  );
}

export default App;
