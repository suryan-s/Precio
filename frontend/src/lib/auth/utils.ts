import { apiUrlBase } from "@/lib/config";
/**
 * Function to fetch data from api with fetch api with auth token from localstorage in header, and uses baseurl. If token is not present or expired, it will throw an error.
 */

export const fetchWithToken = async (url: string, options?: RequestInit) => {
  const token = localStorage.getItem("token");
  if (!token) {
    throw new Error("No token found");
  }
  const res = await fetch(`${apiUrlBase}${url}`, {
    ...options,
    headers: {
      ...options?.headers,
      Authorization: `Bearer ${token}`,
    },
  });
  if (res.status === 401) {
    throw new Error("Token expired");
  }
  return res;
};
