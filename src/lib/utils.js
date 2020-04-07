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

const dataFactory = { stringToNumber };

export { dataFactory };
