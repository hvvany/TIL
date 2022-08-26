-- 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
-- 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.
SELECT * FROM playlist_track AS 'A' ORDER BY PlaylistId DESC LIMIT 5;

-- 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
-- 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
SELECT * FROM tracks AS 'B' ORDER BY TrackId LIMIT 5;

-- 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
-- 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요.
SELECT PlaylistId, Name FROM tracks INNER JOIN playlist_track
ON tracks.TrackId = playlist_track.TrackId ORDER BY PlaylistId DESC LIMIT 10;

-- 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
-- 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
SELECT PlaylistId, Name FROM playlist_track INNER JOIN tracks
ON tracks.TrackId = playlist_track.TrackId ORDER BY Name DESC LIMIT 5;

-- 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을
-- `INNER JOIN`해서 데이터를 출력하세요.
-- 단, 행의 개수만 출력하세요.
SELECT COUNT(*) FROM tracks INNER JOIN artists ON tracks.Composer = artists.Name;

-- 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을
-- `LEFT JOIN`해서 데이터를 출력하세요.
-- 단, 행의 개수만 출력하세요.
SELECT COUNT(*) FROM tracks LEFT JOIN artists ON tracks.Composer = artists.Name;

-- 8. invoice_items 테이블의 데이터를 출력하세요.
-- 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
SELECT InvoiceLineId, InvoiceId FROM invoice_items ORDER BY InvoiceId LIMIT 5;

-- 9. invoices 테이블의 데이터를 출력하세요.
-- 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
SELECT InvoiceId, CustomerId FROM invoices ORDER BY InvoiceId LIMIT 5;

-- 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
-- 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
SELECT InvoiceLineId, invoice_items.InvoiceId  FROM invoice_items
JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId 
ORDER BY invoice_items.InvoiceId DESC LIMIT 5;

-- 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
-- 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
SELECT invoices.InvoiceId, invoices.CustomerId FROM invoices
JOIN customers ON invoices.CustomerId = customers.CustomerId
ORDER BY invoices.InvoiceId DESC LIMIT 5;

-- 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를
-- 모두 함께 출력하세요.
-- 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
SELECT invoice_items.InvoiceLineId, invoice_items.InvoiceId, invoices.CustomerId
FROM invoice_items JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
ORDER BY invoices.InvoiceId DESC LIMIT 5;

-- 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
-- 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 
-- 5개만 출력하세요.
SELECT
    C.CustomerId,
    COUNT(*) AS "개수"
FROM invoice_items AS II 
    INNER JOIN invoices AS I
        ON II.InvoiceId = I.InvoiceId
    INNER JOIN customers AS C
        ON I.CustomerId = C.CustomerId
GROUP BY C.CustomerId
ORDER BY C.CustomerId ASC
LIMIT 5;