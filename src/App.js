import React, { Component } from 'react';
import {Button} from '@material-ui/core';
import Axios from 'axios';

// ran into this issue (hence no npm import of bokehjs):
// https://github.com/bokeh/bokeh/issues/8197

class App extends Component {
  handlePlot1 = () => {
    Axios.get("http://localhost:5000/plot1").then(resp => window.Bokeh.embed.embed_item(resp.data, 'testPlot'))
  }

  handlePlot2 = () => {
    Axios.get("http://localhost:5000/plot2").then(resp => window.testPlot2 = window.Bokeh.embed.embed_item(resp.data, 'testPlot'))
  }

  render() {
    return (
      <div className="App" style={{margin: 20}}>
         Hello World
        <Button variant="contained" style={{margin: 10}} color="primary" onClick={this.handlePlot1}>
          Get Plot 1 
        </Button>
        <Button variant="contained" style={{margin: 10}} color="primary" onClick={this.handlePlot2}>
          Get Plot 2
        </Button>
        <div id='testPlot' className="bk-root"></div>
      </div>
    );
  }
}

export default App;
