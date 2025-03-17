// Define the reportWebVitals function, which measures web performance metrics
const reportWebVitals = onPerfEntry => {
  // Check if onPerfEntry is a function before proceeding
  if (onPerfEntry && onPerfEntry instanceof Function) {
     // Dynamically import the 'web-vitals' library to measure performance metrics
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

export default reportWebVitals;
