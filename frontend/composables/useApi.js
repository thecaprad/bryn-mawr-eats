const METHOD_POST = 1;
const METHOD_GET = 2;
const METHOD_DELETE = 3;
const METHOD_PATCH = 4;

export const useApi = () => {
  const makeRequest = async (url, method, data = null) => {
    const { apiBase } = useConfigVariables();
    const headers = {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    };
    const options = {
      headers: headers,
    };

    switch (method) {
      case METHOD_POST:
        options.method = 'POST';
        break;
      case METHOD_GET:
        options.method = 'GET';
        break;
      case METHOD_DELETE:
        options.method = 'DELETE';
        break;
      case METHOD_PATCH:
        options.method = 'PATCH';
        break;
    }

    if (data) {
      options.body = JSON.stringify(data);
    }
    return await fetch(apiBase + url, options);
  };

  const makePostRequest = async (url, data = null) => {
    return await makeRequest(url, METHOD_POST, data);
  };

  const makeGetRequest = async (url, data = null) => {
    return await makeRequest(url, METHOD_GET, data);
  };

  const makeDeleteRequest = async (url, data = null) => {
    return await makeRequest(url, METHOD_DELETE, data);
  };

  const makePatchRequest = async (url, data = null) => {
    return await makeRequest(url, METHOD_PATCH, (data = data));
  };

  return {
    makePostRequest,
    makeGetRequest,
    makeDeleteRequest,
    makePatchRequest,
  };
};
