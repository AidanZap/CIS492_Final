const Request = async (urlString, restMethod, params) => {

    let url = new URL(urlString);
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))

    const response = await fetch(url.toString(), {
        method: restMethod,
        headers: {
            "Content-Type": "application/json"
        }
    });
  
    return response;
}

export const pipeline = async (country, media, time_period, rating, duration, genre) => {
    let params = {};
    if (country !== null) params["country"] = country;
    if (media !== null) params["type"] = media;
    if (time_period !== null) params["time_period"] = time_period;
    if (rating !== null) params["rating"] = rating;
    if (duration !== null) params["duration"] = duration;
    if (genre !== null) params["genre"] = genre.replace("'", "''");
    let result = await Request("http://localhost:5000/pipeline", "GET", params);
    if (result.ok) return await result.json();
    throw new Error(result.text())
}