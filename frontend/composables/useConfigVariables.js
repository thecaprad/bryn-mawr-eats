export const useConfigVariables = () => {
    const runtimeConfig = useRuntimeConfig();
    const apiBase = runtimeConfig.public.apiBase;
    return {
        apiBase,
    }
  };