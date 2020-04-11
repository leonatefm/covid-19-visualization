import "./App.scss";
import * as React from "react";
import Chart from "../Chart";
import { dataFactory } from "../../lib/utils";
import { Layout } from "antd";
import dataset from "../../data/world_aggregated.json";

const { Header, Footer, Content } = Layout;
const data = dataset.filter((data) => data.type !== "increase_rate");

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
                data: dataFactory.stringToNumber(data, ["value"]),
                xField: "date",
                xAxis: {
                  type: "dateTime",
                },
                yField: "value",
                yAxis: {
                  tickInterval: 200000,
                  label: {
                    formatter: (label, data) => {
                      return dataFactory.numberFormat({ notation: "compact", compactDisplay: "short" }).format(data.id);
                    },
                  },
                },
                seriesField: "type",
                meta: {
                  type: {
                    formatter: (v) => {
                      return dataFactory.formatLabel(v);
                    },
                  },
                  value: {
                    formatter: (v) => {
                      return dataFactory.numberFormat().format(v);
                    },
                  },
                },
                legend: {
                  position: "right-top",
                },
                animation: {
                  appear: {
                    duration: 3000,
                  },
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
