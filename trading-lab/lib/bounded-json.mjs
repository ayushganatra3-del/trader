export async function boundedJSON(message, limit) {
  if (Number(message.headers.get('content-length') || 0) > limit) throw Error('Record exceeds the storage limit.');
  const reader = message.body?.getReader();
  if (!reader) throw Error('Missing JSON record.');
  const decoder = new TextDecoder();
  let size = 0, text = '';
  try {
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      size += value.byteLength;
      if (size > limit) { await reader.cancel(); throw Error('Record exceeds the storage limit.'); }
      text += decoder.decode(value, { stream: true });
    }
    return JSON.parse(text + decoder.decode());
  } finally { reader.releaseLock(); }
}
