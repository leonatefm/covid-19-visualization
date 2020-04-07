import "./App.scss";
import * as React from "react";
import { Layout } from "antd";

const { Header, Footer, Content } = Layout;

function App() {
  return (
    <div className="App">
      <Layout className="App-layout">
        <Header className="App-header">COVID 19 Visualization</Header>
        <Content className="App-content"></Content>
        <Footer className="App-footer">Designed by Z&Z &copy;2020</Footer>
      </Layout>
    </div>
  );
}

export default App;
