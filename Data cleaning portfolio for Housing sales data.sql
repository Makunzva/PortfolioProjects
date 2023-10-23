Select *
From PortfolioProject..[NashvilleHousing ]

-- Standardising the date format
Select SaleDate, CONVERT(Date,SaleDate)
From PortfolioProject..[NashvilleHousing ]


ALTER TABLE PortfolioProject..[NashvilleHousing ]
ADD SaleDateConverted Date 

Update [NashvilleHousing ]
Set SaleDateConverted = CONVERT(Date,SaleDate)

-- Populate property address data
Select *
From PortfolioProject..[NashvilleHousing ]
--WHERE PropertyAddress IS NULL
ORDER BY ParcelID

Select a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress, b.PropertyAddress)
From PortfolioProject..[NashvilleHousing ] a
JOIN PortfolioProject..[NashvilleHousing ] b
ON a.ParcelID = b.ParcelID
AND a.[UniqueID ]<> b.[UniqueID ]
WHERE a.PropertyAddress IS NULL

UPDATE a
SET PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress)
From PortfolioProject..[NashvilleHousing ] a
JOIN PortfolioProject..[NashvilleHousing ] b
ON a.ParcelID = b.ParcelID
AND a.[UniqueID ]<> b.[UniqueID ]
WHERE a.PropertyAddress IS NULL


--start
-- Breaking out address into individual columns (Adress, City, State)

Select PropertyAddress
From PortfolioProject..[NashvilleHousing ]

SELECT 
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PortfolioProject..[NashvilleHousing ].PropertyAddress ) -1) AS Address
, SUBSTRING(PropertyAddress, CHARINDEX(',', PortfolioProject..[NashvilleHousing ].PropertyAddress) +1, LEN(PropertyAddress)) AS Address
FROM PortfolioProject..[NashvilleHousing ]


--Creating the columns and inserting data one at a time
ALTER TABLE PortfolioProject..[NashvilleHousing ]
ADD PropertySplitAddress nvarchar(255) 

Update [NashvilleHousing ]
Set PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PortfolioProject..[NashvilleHousing ].PropertyAddress ) -1)


ALTER TABLE PortfolioProject..[NashvilleHousing ]
ADD PropertySplitCity nvarchar(255) 

Update [NashvilleHousing ]
Set PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PortfolioProject..[NashvilleHousing ].PropertyAddress) +1, LEN(PropertyAddress))

--End of split

-- Using parsename to split
Select OwnerAddress
From PortfolioProject..[NashvilleHousing ]

SELECT 
PARSENAME(REPLACE(OwnerAddress, ',','.'), 3)
,PARSENAME(REPLACE(OwnerAddress, ',','.'), 2)
,PARSENAME(REPLACE(OwnerAddress, ',','.'), 1)
From PortfolioProject..[NashvilleHousing ]

--Creating tables and inserting data
ALTER TABLE PortfolioProject..[NashvilleHousing ]
ADD OwnerSplitAddress nvarchar(255) 

Update [NashvilleHousing ]
Set OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',','.'), 3)

ALTER TABLE PortfolioProject..[NashvilleHousing ]
ADD OwnerSplitCity nvarchar(255) 

Update [NashvilleHousing ]
Set OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',','.'), 2)

ALTER TABLE PortfolioProject..[NashvilleHousing ]
ADD OwnerSplitState nvarchar(255) 

Update [NashvilleHousing ]
Set OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',','.'), 1)

-- End of split using parsename

Select *
From PortfolioProject..[NashvilleHousing ]

-- Changing Y and N to Yes and No

Select DISTINCT(SoldAsVacant)
From PortfolioProject..[NashvilleHousing ]

SELECT SoldAsVacant
, CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
		WHEN SoldAsVacant = 'N' THEN 'No'
		ELSE SoldAsVacant
		END
From PortfolioProject..[NashvilleHousing ]

UPDATE PortfolioProject..[NashvilleHousing ]
SET SoldAsVacant = CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
		WHEN SoldAsVacant = 'N' THEN 'No'
		ELSE SoldAsVacant
		END
-- the end

--Removing dublicates in the table

WITH RowNumCTE AS (
SELECT *, 
	ROW_NUMBER() OVER (
	PARTITION BY	ParcelID,
					PropertyAddress,
					SalePrice,
					SaleDate,
					LegalReference
					ORDER BY 
						UniqueID
						) ROW_NUM
FROM PortfolioProject..[NashvilleHousing ]
)
SELECT *
From RowNumCTE
WHERE ROW_NUM > 1
ORDER BY PropertyAddress


WITH RowNumCTE AS (
SELECT *, 
	ROW_NUMBER() OVER (
	PARTITION BY	ParcelID,
					PropertyAddress,
					SalePrice,
					SaleDate,
					LegalReference
					ORDER BY 
						UniqueID
						) ROW_NUM
FROM PortfolioProject..[NashvilleHousing ]
)
DELETE 
From RowNumCTE
WHERE ROW_NUM > 1

-- end of removing duplicates


-- Deleting unwanted columns

SELECT *
FROM PortfolioProject..[NashvilleHousing ]

ALTER TABLE PortfolioProject..[NashvilleHousing ]
DROP COLUMN PropertyAddress, TaxDistrict, OwnerAddress

ALTER TABLE PortfolioProject..[NashvilleHousing ]
DROP COLUMN SaleDate

-- End of column deleting


