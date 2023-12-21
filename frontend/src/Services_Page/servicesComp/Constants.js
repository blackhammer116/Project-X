export const URL = "http://localhost:5000";
export const AUTHURL = "http://localhost:4000";
export const getKeyByValue = (obj, value) => {
  return Object.keys(obj).find((key) => obj[key] === value);
};
