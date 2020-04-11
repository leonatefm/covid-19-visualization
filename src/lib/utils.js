const stringToNumber = (data, fields) => {
  if (!data || !fields || !data.length || !fields.length) {
    return data;
  }
  const result = data.map((item) => {
    fields.forEach((field) => {
      if (item.hasOwnProperty(field)) {
        const value = item[field];
        const newValue = !Number.isNaN(Number(value)) ? Number(value) : 0;
        item[field] = newValue;
      }
    });
    return item;
  });
  return result;
};

const formatLabel = (str) => {
  const result = str.replace(/_/g, " ").replace(/^./, str[0].toUpperCase());
  return result;
};

const locale = navigator && navigator.language ? navigator.language : "en-US";
const numberFormat = (options) => {
  return new Intl.NumberFormat(locale, options);
};

const dataFactory = { stringToNumber, formatLabel, numberFormat };

export { dataFactory };
