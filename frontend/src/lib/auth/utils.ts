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
      Authorization: `Bearer ${token}`,
    },
  });
  if (res.status === 401) {
    throw new Error("Token expired");
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
): [Error | undefined, T | undefined] => {
  const [data, setData] = useState<any>();
  const [error, setError] = useState<any>();
  const [, setLocation] = useLocation();
  useEffect(() => {
    fetchWithToken(url, options)
      .then((res) => res.json())
      .then((data) => {
        setData(data);
      })
      .catch((e) => {
        setError(e);
        if (e.message === "Token expired" || e.message === "No token found") {
          localStorage.removeItem("token");
          setLocation("/login");
        }
      });
  }, [url, options]);
  return [error, data];
};
