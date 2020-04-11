import "./Chart.scss";
import * as React from "react";
import * as g2plot from "@antv/g2plot";

class Chart extends React.PureComponent {
  componentDidMount() {
    const { config, id, type } = this.props;
    const chart = new g2plot[type](id, config);
    chart && chart.render();
  }
  render() {
    const { id } = this.props;
    return (
      <section className="Chart">
        <div id={id} />
      </section>
    );
  }
}

export default Chart;
