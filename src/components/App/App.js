import "./App.scss";
import * as React from "react";
import Chart from "../Chart";
import { dataFactory } from "../../lib/utils";
import { Layout } from "antd";
import dataset from "../../data/world_aggregated.json";

const { Header, Footer, Content } = Layout;

class App extends React.PureComponent {
  render() {
    return (
      <div className="App">
        <Layout className="App-layout">
          <Header className="App-header">COVID 19 Visualization</Header>
          <Content className="App-content">
            <Chart
              id="world_aggregated"
              type="Line"
              config={{
                title: {
                  visible: true,
                  text: "World aggregated cases",
                },
                description: {
                  visible: true,
                  text: "This chart visualizes the trend of confirmed, recovered and death cases worldwide.",
                },
                data: dataFactory.stringToNumber(dataset, ["confirmed", "recovered", "deaths", "increase_rate"]),
                xField: "date",
                yField: "confirmed",
                point: {
                  visible: true,
                },
              }}
            />
          </Content>
          <Footer className="App-footer">Designed by Z&Z &copy;2020</Footer>
        </Layout>
      </div>
    );
  }
}

export default App;
