import axios from 'axios';
import React from 'react';

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
        <header>Data generated from Django</header>
        <hr></hr>
        {this.state.details.map((e, id) => (
          <div key={id}>
            <p>{e.employee}</p>
            <p>{e.department}</p>
            <br/>
          </div>
        ) )}
      </div>
    )
  }

}

export default App;