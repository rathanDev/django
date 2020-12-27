import React, { Component } from 'react';

class Login extends Component {


    render() {
        return (
            <div>
                Username: <input type="text" /> <br />
                Password: <input type="text" /> <br />
                <input type="submit" value="Login" onClick={this.login} />
            </div>
        )
    }

    login() {
        console.log('login button clicked');

        const url = 'http://localhost:8000/api-token-auth/';

        //const requestOptions = {};
        const requestOptions = {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(
                {
                    username: 'jana',
                    password: 'jana@123'
                }
            )
        };

        fetch(url, requestOptions)
            .then(res => res.json())
            .then((data) => {
                console.log('data', data);
                
            })
            .catch(console.error);

    }

}

export default Login;