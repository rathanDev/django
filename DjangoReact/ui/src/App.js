import axios from 'axios';
import React from 'react';
import './App.css'

class App extends React.Component {

  state = { details : [] };

  componentDidMount() {
    let data;
    axios.get('http://localhost:8000')
      .then(res => {
        data = res.data;
        this.setState({
          details : data
        });
      })
      .catch(err => {
        console.error(err);
      });
  }

  render() {
    return (
      <div>
        <body>
          <header>Data generated from Django</header>
          <hr></hr>
          {this.state.details.map((e, id) => (
            <div key={id}>
              <p>{e.employee}</p>
              <p>{e.department}</p>
              <br/>
            </div>
          ) )}
        </body>
      </div>
    )
  }

}

export default App;