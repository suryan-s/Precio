import { apiUrlBase } from "@/lib/config";
import { useState, useEffect } from "react";
import { useLocation } from "wouter";

/**
 * Function to fetch data from api with fetch api with auth token from localstorage in header, and uses baseurl. If token is not present or expired, it will throw an error.
 * @param url - url to fetch from
 * @param options - options to pass to fetch api
 */
export const fetchWithToken = async (
  url: string,
  options?: RequestInit
): Promise<Response> => {
  const token = localStorage.getItem("token");
  if (!token) {
    throw new Error("No token found");
  }
  const res = await fetch(`${apiUrlBase}${url}`, {
    ...options,
    headers: {
      ...options?.headers,
      "Content-Type": "application/json",
      Authorization: `Bearer ${JSON.parse(token)}`,
    },
  });
  if (res.status === 401) {
    throw new Error("Token expired");
  }
  if (res.status === 500) {
    throw new Error("Server error");
  }
  return res;
};

/**
 *  React hook to fetch data from api with fetch api with auth token from localstorage in header, and uses baseurl. If token is not present or expired, it will return an error. It will also return the data.
 * @param url - url to fetch from
 * @param options - options to pass to fetch api
 */
export const useFetchWithToken = <T = any>(
  url: string,
  options?: RequestInit
): [Error | undefined, T | undefined, boolean] => {
  const [data, setData] = useState<any>();
  const [error, setError] = useState<any>();
  const [loading, setLoading] = useState<boolean>(true);
  const [, setLocation] = useLocation();
  useEffect(() => {
    const abortController = new AbortController();
    setLoading(true);
    fetchWithToken(url, {
      ...options,
      signal: abortController.signal,
    })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        setLoading(false);
        console.log(data);
        setData(data);
      })
      .catch((e) => {
        setError(e);
        setLoading(false);
        if (e.message === "The user aborted a request.") {
          setLoading(true);
        }
        if (e.message === "Token expired" || e.message === "No token found") {
          localStorage.removeItem("token");
          setLocation("/login");
        }
      });
    return () => {
      abortController.abort();
    };
  }, [url, options]);
  return [error, data, loading];
};
